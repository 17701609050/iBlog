# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Time    : 18-5-11 下午5:26
# @Author  : Ziping
# @Email   : zipingx.lv@intel.com
# @Project : Automation-Hub
# -----------------------------------------------------
import re
import json
from collections import OrderedDict
from django.middleware import csrf
from django.conf import settings
from django.core.cache import cache
from django.core.urlresolvers import reverse
from .treelib import Tree
from .models import *


class SessionArgs(object):
    ENCRYPT_KEY = 119  # encrypt number key
    ENCRYPT_STRING = '***_icg_***'  # encrypt string
    USER_TOKEN = 'sessionid'  # user cookie key
    STAFF_TOKEN = 'IDSID'  # staff idsid cookie key
    UNAME_KEY = 'u_name'  # login name
    AUTHOR_ROLES = "author_role"  # login user author list
    SYS_MENU_HTML = 'sys_menu_html'  # login user menu string
    SYS_MENU_LIST = 'sys_menu_list'  # login user function string
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


class SysRoleService(BaseService):
    def __init__(self, clazz):
        super(SysRoleService, self).__init__(clazz)
        self.clazz = SysMRole

    def findRoleIDByCodes(self, roleCodes):
        return self.clazz.objects.filter(interface_name__in=roleCodes).values('role_code','remark')

    def getDistinctRoleNames(self):
        return self.clazz.objects.values('role_code', 'role_name_en', 'interface_name').distinct().order_by('role_code')

    def deleteByIDs(self, pks, logUser):
        return BaseService.deleteByIDs(self, self.clazz, pks, logUser)

    def count(self, args):
        return BaseService.count(self, self.clazz, **args)


class SysFunService(BaseService):
    def __init__(self, clazz):
        super(SysFunService, self).__init__(clazz)
        self.clazz = SysMFun

    def find_list(self):
        return BaseService.find_list(self, self.clazz)

    def count(self, args):
        return BaseService.count(self, self.clazz, **args)

    def create(self, args):
        return BaseService.create(self, self.clazz, **args)

    def update(self, pk, args):
        return BaseService.update(self, self.clazz, pk, **args)

    def deleteByIDs(self, pks, logUser):
        return BaseService.deleteByIDs(self, self.clazz, pks, logUser)


class SysAuthService(BaseService):
    def __init__(self, clazz):
        super(SysAuthService, self).__init__(clazz)
        self.clazz = SysMAuthority

    def findDinMenuCodeByMutilRole(self, roleCodes):
        """按复合的权限编号，取得唯一菜单编号"""
        return self.clazz.objects.filter(role_code__in=roleCodes).values('menu_code').distinct()

    def findDinMenuFunByMutilRole(self, roleCodes=None):
        """按复合的权限编号，取得唯一菜单编号"""
        # TIP: MYSQL Group_Concat Length limit
        menu_funcs = self.clazz.objects.filter(role_code__in=roleCodes).values('menu_code')\
            .annotate(fun_codes=GroupConcat('fun_codes')).order_by('menu_code')

        menu_funcs_dict = {}
        for menu_func in menu_funcs:
            menu_funcs_dict[menu_func['menu_code']] = []
            if menu_func['fun_codes']:
                menu_func['fun_codes'] = menu_func['fun_codes'].strip()
                for fun_code in re.split(r'[;,\s]+', menu_func['fun_codes']):
                    if fun_code and fun_code != ',' and fun_code != ';':
                        menu_funcs_dict[menu_func['menu_code']].append(fun_code)
        return menu_funcs_dict

    def find_menu_code(self, rolecode):
        menu_list = self.clazz.objects.filter(role_code=rolecode).values('menu_code')
        return [menu['menu_code'] for menu in menu_list if menu_list]


class SysMenuService(BaseService):
    def __init__(self, clazz=None):
        super(SysMenuService, self).__init__(clazz)
        self.clazz = SysMMenu

    def findActiveMenu(self):
        return self.clazz.objects.filter(visible=1).order_by('menu_code', 'parent_code')

    def find_list(self):
        return BaseService.find_list(self, self.clazz, *('menu_code', 'parent_code'))

    def count(self, args):
        return BaseService.count(self, self.clazz, **args)

    def create(self, args):
        return BaseService.create(self, self.clazz, **args)

    def update(self, pk, args):
        return BaseService.update(self, self.clazz, pk, **args)

    def deleteByIDs(self, pks, logUser):
        return BaseService.deleteByIDs(self, self.clazz, pks, logUser)

    def get_menu_node_tree_by_root(self, menu_code_list):
        menu_tree_dict = OrderedDict()
        all_menu = []
        for menu_code in menu_code_list:
            all_menu.append(SysMMenu.objects.filter(menu_code=menu_code).order_by('menu_order_num', 'menu_code', 'parent_code').get())
        for menu in all_menu:
            if menu.parent_code is not None and menu.parent_code.strip() != '':
                # child menu
                menu_root = menu.menu_code[:3]  # menu code style limit
                # if menu.menu_code == 'M0201':
                #     if menu_tree_dict.get(menu_root) and menu_tree_dict[menu_root].contains(menu.parent_code):
                #         menu.menu_name_en = '${**MENU**MOUNT**}'
                #         menu_tree_dict[menu_root].create_node(menu, menu.menu_code, parent=menu.parent_code)
                #     continue
                if menu_tree_dict.get(menu_root) and menu_tree_dict[menu_root].contains(menu.parent_code):
                    menu_tree_dict[menu_root].create_node(menu, menu.menu_code, parent=menu.parent_code)
            else:
                # parent menu
                menu_tree = Tree()
                menu_tree.create_node(menu, menu.menu_code)
                menu_tree_dict[menu.menu_code] = menu_tree
        return menu_tree_dict

    def get_menus_html(self, menu_tree_list):
        menu_html, expended_node = [], []
        # More trees Expand
        for root_code, menu_tree in menu_tree_list.items():
            # One trees Expand
            for nid in menu_tree.expand_tree():
                menu_node = menu_tree.get_node(nid)
                # if menu_node.identifier in user_auth_list:
                main_menu = menu_node.tag
                if menu_node.identifier not in expended_node:
                    # append first node
                    if main_menu.menu_name_en.startswith('${**') and main_menu.menu_name_en.endswith('**}'):
                        menu_html.append(main_menu.menu_code)
                    else:
                        menu_html.append(
                            '<li{*{' + main_menu.menu_code + 'submenu}*} menu_code="' + main_menu.menu_code +
                            '" menu_recommend="' + str(main_menu.recommended) + '"><a '
                            + ('style="' + main_menu.menu_style + '" ' if main_menu.menu_style else '') + 'href="'
                            + url_reverse(main_menu.menu_url) + '"{*{' + main_menu.menu_code +
                            'down}*}><span>' + main_menu.menu_name_en + '</span>{*{' + main_menu.menu_code +
                            'claz}*}</a>{*{' + main_menu.menu_code + 'others}*}</li>')
                    expended_node.append(menu_node.identifier)  # node expended

                    # check has child node
                menu_branch = menu_tree.is_branch(menu_node.identifier)
                # get user child node
                # menu_branch = list(set(user_auth_list.keys()).intersection(set(menu_branch)))
                menu_branch.sort()  # sort menu
                if menu_branch:
                    menu_html = ''.join(menu_html)
                    if root_code == menu_node.identifier:  # first menu
                        menu_html = menu_html.replace('{*{' + main_menu.menu_code + 'claz}*}',
                                                      '<span class="caret"></span>'). \
                            replace('{*{' + main_menu.menu_code + 'submenu}*}', '')
                    else:
                        menu_html = menu_html.replace('{*{' + main_menu.menu_code + 'claz}*}', '') \
                            .replace('{*{' + main_menu.menu_code + 'submenu}*}', ' class="dropdown-submenu"')

                    menu_html = menu_html.replace('{*{' + main_menu.menu_code + 'down}*}',
                                                  ' data-toggle="dropdown" class="dropdown-toggle"')
                    menu_html = [menu_html, ]

                    # Sub menu
                    sub_menu_list = ['<ul class="dropdown-menu">', ]
                    for mb in menu_branch:
                        sub_menu = menu_tree.get_node(mb).tag
                        if sub_menu.menu_name_en.startswith('${**') and sub_menu.menu_name_en.endswith('**}'):
                            sub_html = sub_menu.menu_name_en
                        else:
                            sub_html = '<li{*{' + sub_menu.menu_code + 'submenu}*} menu_mark="' + str(
                                sub_menu.menu_mark) + \
                                       '" last_update_time="' + str(
                                sub_menu.last_update_time) + '" watch="' + sub_menu.menu_name_en + \
                                       '" auto_expire="' + str(
                                sub_menu.auto_expire) + '" effective_time_interval="' + \
                                       str(
                                           sub_menu.effective_time_interval) + '" menu_code="' + sub_menu.menu_code + '" menu_recommend="' + \
                                       str(sub_menu.recommended) + '"><a ' + (
                                           'style="' + sub_menu.menu_style + '" ' if sub_menu.menu_style else '') + \
                                       'href="' + url_reverse(sub_menu.menu_url) + '">' + \
                                       sub_menu.menu_name_en + '</a>{*{' + sub_menu.menu_code + 'others}*}</li>'
                        sub_menu_list.append(sub_html)  # node expended
                        expended_node.append(mb)

                    sub_menu_list.append('</ul>')
                    sub_menu_list = ''.join(sub_menu_list)

                    menu_html = ''.join(menu_html)
                    menu_html = menu_html.replace('{*{' + main_menu.menu_code + 'others}*}', sub_menu_list)
                    menu_html = [menu_html, ]
                else:
                    menu_html = ''.join(menu_html)
                    menu_html = menu_html.replace('{*{' + main_menu.menu_code + 'submenu}*}', '') \
                        .replace('{*{' + main_menu.menu_code + 'down}*}', '') \
                        .replace('{*{' + main_menu.menu_code + 'claz}*}', '') \
                        .replace('{*{' + main_menu.menu_code + 'others}*}', '')
                    menu_html = [menu_html, ]
        return ''.join(menu_html)


class DjLogLoginService(BaseService):
    def __init__(self, clazz):
        super(DjLogLoginService, self).__init__(clazz)
        # self.clazz = DjLogLogin

    def getSessionData(self, request):
        if settings.SESSION_ENGINE_ALIAS == 'redis':
            return cache.get(request.session[SessionArgs.USER_TOKEN])
        else:
            s = DjLogSessionData.objects.filter(session_key=request.session[SessionArgs.USER_TOKEN]).first()
            return s.get_decoded_data()

def url_reverse(urlkey, **kwargs):
    """ To obtain the corresponding absolute addresses menu
    :param urlkey: URL name
    :return: absolute addresses
    """
    try:
        return reverse(urlkey, **kwargs)
    except:
        if '?' not in urlkey and '#' not in urlkey and not urlkey.endswith('/'):
            urlkey += '/'
        return urlkey

def url_rules_match(req):

    visit_url = req.path

    # common URL(login/logout/403/404/500/api URL)
    if visit_url.strip('/') in ('admin', 'login', 'logout', '401', '403', '404', '500', 'rest/login', 'rest/help', 'home'):
        return False

    # api URL, set CSRF Token
    if visit_url.startswith('/rest/'):
        req.META['HTTP_X_CSRFTOKEN'] = req.COOKIES.get('csrftoken', csrf.get_token(req))

    # admin URL
    if visit_url.startswith('/admin/'):
        return False

    return True

def string2JSON(str_json):
    if isinstance(str_json, dict):
        return str_json

    json_obj = {}
    if str_json:
        try:
            json_obj = json.loads(str_json)
        except:
            try:
                json_obj = eval(str_json)
            except:
                pass
        finally:
            return json_obj
    else:
        return json_obj