# -*- coding: UTF-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import timezone
from .models import SysRPermissionUser

class SessionArgs(object):
    ENCRYPT_KEY = 119  # encrypt number key
    ENCRYPT_STRING = '***_icg_***'  # encrypt string
    USER_TOKEN = 'sessionid'  # user cookie key
    STAFF_TOKEN = 'IDSID'  # staff idsid cookie key
    UNAME_KEY = 'u_name'  # login name
    AUTHOR_ROLES = "author_role"  # login user author list
    SYS_MENU_HTML = 'sys_menu_html'  # login user menu string
    SYS_FUN_LIST = 'sys_fun_list'  # login user function string
    SYS_USER_CONFIG = 'sys_user_config'  # login user customize configuration
    USER_ROLE_MENU_FILTER = 'user_role_menu_filter'  # filter the menu's regular expression
    X_USER_ORIGIN = 'ICG_REST_API'
    # admin list
    SUPPER_ADMIN = 'icgadmin'
    ADMIN_LIST = ('icgadmin', 'admin',)
    ANONYMOUS_ROLE = 'anonymous'
    CATEGORY_OWNER = 'session_map'
    USER_BLACKLIST_PREFIX = 'USER_BLACKLIST:'

class BaseService(object):
    def __init__(self, clazz):
        self.clazz = clazz

    def get(self, pk, m=None):
        """Entity object by primary key query
         :param pk: primary key
         :return: to query the entity objects
        """
        m = m if m else self.clazz
        try:
            m1 = self.clazz.objects.get(pk=pk)
        except m.DoesNotExist:
            m1 = None
        return m1

    def fetch(self, conds):
        """Conditional query entity object
        :param conds: query conditional
        :return: to query the entity objects
        """
        try:
            m1 = self.clazz.objects.get(**conds)
        except self.clazz.MultipleObjectsReturned:
            m1 = self.clazz.objects.filter(**conds).first()
        except self.clazz.DoesNotExist:
            m1 = None
        return m1

    def find(self, m):
        """ Find an object
         :param m: Condition of object lookup
         :return: the result set
        """
        result = None
        try:
            result = m.__class__.objects.get(pk=m.pk)
        except m.__class__.DoesNotExist:
            result = None
        except Exception, e:
            # logging.getLogger('django').info(e)
            raise e
        finally:
            return result

    def find_all(self, m=None):
        """ Find all
         :param m: table objects
         :return: the result set
        """
        result = None
        try:
            m = m and m.__class__ or self.clazz
            result = m.objects.all()
        except Exception, e:
            # logging.getLogger('django').info(e)
            raise e
        finally:
            return result

    def filter_list(self, m, usedFieldNameList=None, *order, **args):
        """Find an object
          :param m: Condition of object lookup
        """
        result = None
        try:
            if not args:
                for field in m._meta.fields:
                    if field.name in usedFieldNameList:
                        args[field.name] = getattr(m, field.name)
            if order:
                result = m.__class__.objects.filter(**args).order_by(*order)
            else:
                result = m.objects.filter(**args)  # m.__class__
        except Exception, e:
            # logging.getLogger('django').error(e)
            raise e
        finally:
            return result



    def find_list(self, m, *order):
        """ Find a collection of objects QuerySet
           :param m: Criteria object m looking
        """
        if order:
            return m.objects.all().order_by(*order)
        else:
            return m.objects.all()

    def create(self, m, **argz):
        """ Conditions created by the combination of
            :param m: Entity Object
        """
        pk_args = {}
        fk_suffix = "_id"
        for field in m._meta.fields:
            if field.name in argz:
                pk_args[field.name] = argz[field.name]
            else:
                if field.get_internal_type().lower() == "foreignkey":
                    fk_name = field.name + fk_suffix
                    if fk_name in argz:
                        pk_args[fk_name] = argz[fk_name]

        return m.objects.create(**pk_args)

    def update(self, m, pk, **argz):
        """ Conditional update
        :param m: Entity Object
        :param pk: Primary key
        """
        pk_args = {}
        fk_suffix = "_id"
        for field in m._meta.fields:
            if field.name in argz:
                pk_args[field.name] = argz[field.name]
            else:
                if field.get_internal_type().lower() == "foreignkey":
                    fk_name = field.name + fk_suffix
                    if fk_name in argz:
                        pk_args[fk_name] = argz[fk_name]

        return m.objects.filter(pk=pk).update(**pk_args)

    def update_by_fk(self, fk, **argz):
        """ Conditional update
        :param fk: Foreign key
        """
        pk_args = {}
        fk_suffix = "_id"
        for field in self.clazz._meta.fields:
            if field.name in argz:
                pk_args[field.name] = argz[field.name]
            else:
                if field.get_internal_type().lower() == "foreignkey":
                    fk_name = field.name + fk_suffix
                    if fk_name in argz:
                        pk_args[fk_name] = argz[fk_name]
        qs = self.clazz.objects.filter(**fk)
        if len(qs) > 0:
            return qs.update(**pk_args)
        else:
            return qs.create(**pk_args)

    def update_cascade(self, m, pk, **argz):
        """ Conditional update
        :param m: Entity Object
        :param pk: Primary key
        """
        m = self.get(pk=pk, m=m)
        pk_args = {}
        for field in m._meta.fields:
            if field.get_internal_type().lower() == "foreignkey":
                foreign_args = {}
                foreign_model = getattr(m, field.name)
                perfix = foreign_model.__class__.__name__.lower() + '_' + field.name
                for arg in argz:
                    foreign_cols = foreign_model._meta.get_all_field_names()
                    foreign_field = arg.replace(perfix, '')
                    if arg.startswith(perfix) and foreign_field in foreign_cols:
                        foreign_args[foreign_field] = argz[arg]
                foreign_model.update(**foreign_model)
            else:
                if field.name in argz:
                    pk_args[field.name] = argz[field.name]

        m.update(**argz)
        return m

class SysPermUserService(BaseService):
    def __init__(self, clazz):
        super(SysPermUserService, self).__init__(clazz)
        self.clazz = SysRPermissionUser

    def getUserPermByName(self, userName):
        sysPermUser = SysRPermissionUser()
        sysPermUser.user_name = userName
        return self.find(sysPermUser)

def do_login(request, manual=None):
    """
    :param request: request object
    :param manual: 是否自动登录
    :return: 验证结果
    """
    user_authenticated = False
    session_data = ''
    username = request.REQUEST.get('username', '').strip()
    password = request.REQUEST.get('password', '').strip()
    manual = request.COOKIES.get(SessionArgs.STAFF_TOKEN) is None if manual is None else manual
    # 手动登录，验证登录身份(同时验证用户名+密码).
    if manual:
        # 验证用户名+密码
        user = authenticate(username=username, password=password)
        if user is not None:
            user_authenticated = user.is_active
            if user_authenticated:
                login(request, user)
    else:  # IDSID 直接登录
        # Authenticate from via Circuit
        username = request.COOKIES.get(SessionArgs.STAFF_TOKEN, username)
        if username:
            try:
                user = User._default_manager.get_by_natural_key(username)
            except User.DoesNotExist:
                user = User(username=username,
                            password=password,
                            is_superuser=0,
                            is_active=1,
                            is_staff=0,
                            date_joined=get_utc_now(),
                            last_login=get_utc_now(),
                            first_name=username,
                            last_name=username,
                            email=username+'@intel.com')
                user.save()
            user.backend = 'django_auth_ldap.backend.LDAPBackend'
            login(request, user)
            user_authenticated = True
        else:
            user_authenticated = False

    # 认证通过
    if user_authenticated:
        session_data = build_sso(request)

    return user_authenticated, session_data

def build_sso(request):
    user_role = build_user_role(request)
    return build_user_session(request, user_role)


def build_user_role(request):

    # 如果在session里有用户role的权限(已登录)直接返回当前session_data
    # 否则需要用户名重新去获取用户的role
    if SessionArgs.AUTHOR_ROLES in request.session:
        return request.session[SessionArgs.AUTHOR_ROLES]
    else:
        userRole = sysPermUserService.getUserPermByName(request.user.username)
        if userRole is None:
            # allow anonymous access
            user_role = SessionArgs.ANONYMOUS_ROLE
        else:
            user_role = userRole.user_role
            # everyone is anonymous
            user_role = user_role.strip(',') + ',' + SessionArgs.ANONYMOUS_ROLE

        return user_role


def build_user_session(request, user_role):
    def build_session(req, cache_key, u_role):
        user_role_code = []
        user_role_menu_filter = {}
        for item in sysRoleService.findRoleIDByCodes(u_role.split(',')):
            user_role_code.append(item['role_code'])
            if item['remark'] and str(item['remark']).strip() != '':
                role_menu_filter = string2JSON(item['remark'])
                for menu_filter in role_menu_filter:
                    if menu_filter in user_role_menu_filter:
                        user_role_menu_filter[menu_filter] += "," + role_menu_filter[menu_filter]
                    else:
                        user_role_menu_filter[menu_filter] = role_menu_filter[menu_filter]
        user_auth_list = sysAuthService.findDinMenuFunByMutilRole(user_role_code)
        all_fun_list = {}  # all function dict
        sys_fun_list = []  # all menu list
        for fun_obj in sysFunService.find_list():
            all_fun_list[fun_obj.fun_code] = fun_obj.toDic()
        for sysMenu in sysMenuService.find_list():
            sys_menu_dict = sysMenu.toDic()  # system function list
            sys_menu_dict['functions'] = []
            if sysMenu.menu_code in user_auth_list:
                if user_auth_list.get(sysMenu.menu_code):
                    for fun_code in user_auth_list[sysMenu.menu_code]:
                        sys_menu_dict['functions'].append(all_fun_list.get(fun_code, ''))
                sys_fun_list.append(sys_menu_dict)

        # get tree node
        # is_rest_request = bool(req.META.get('X_USER_ORIGIN') and req.META['X_USER_ORIGIN'])
        # if not is_rest_request: #@bug: REST USER is no separate authority
        menu_tree = sysMenuService.get_menu_node_tree_by_root()
        menu_html_string = get_menus_string_from_session(req, menu_tree, user_auth_list)
        menu_html_string = sysMenuService.get_validation_report_menu_style_string(req, user_auth_list, menu_html_string)

        # save into redis
        return {SessionArgs.SYS_MENU_HTML: menu_html_string,
                SessionArgs.SYS_FUN_LIST: sys_fun_list,
                SessionArgs.AUTHOR_ROLES: user_role,
                SessionArgs.USER_TOKEN: cache_key,
                SessionArgs.ENCRYPT_STRING: request.session.session_key,
                SessionArgs.USER_ROLE_MENU_FILTER: user_role_menu_filter}

    role_cache_key = CACHE_PREFIX + sysCategoryService.saveOrUpdateCategory(SessionArgs.CATEGORY_OWNER, user_role)
    _session_data = build_session(request, role_cache_key, user_role)

    if settings.SESSION_ENGINE_ALIAS == 'redis':
        session_data = cache.get(role_cache_key)
        if session_data is None:
            cache.set(role_cache_key, _session_data, timeout=settings.SESSION_CACHE_TIMEOUT)
    else:
        session_data = DjLogSessionData.objects.filter(session_key=role_cache_key).first()
        if session_data is None:
            session_data = DjLogSessionData()
            session_data.session_key = role_cache_key
            session_data.session_data = _session_data
            session_data.set_encode_data()
            session_data.save()

    # save to session
    request.session[SessionArgs.AUTHOR_ROLES] = _session_data[SessionArgs.AUTHOR_ROLES]
    request.session[SessionArgs.USER_TOKEN] = _session_data[SessionArgs.USER_TOKEN]
    request.session.modified = True  # flush session

    return _session_data

def get_utc_now(str_format=False):
    if str_format:
        return timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        return timezone.now()