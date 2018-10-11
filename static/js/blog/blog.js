/**
 * Created by zipinglx on 18-10-11.
 */
document.write("<script language=javascript src='/static/js/main.js'></script>");

function search_blog(){
    this.blogClass = blog; // main.js中的blog

    this.offset = offset;
    this.limit = limit;
    this.searchUrl = '/rest/blogs/';
    this.funtion_name_list = ['generateBlogList', 'resizeBlogClass'];
}

$(function () {
    var constructor = search_blog;
    obj = new constructor();
    obj.load();
})

search_blog.prototype = {

    urlparames: window.location.href,
    searchKey: getUrlParam("q", this.urlparames),
    pageoffset: getUrlParam("offset", this.urlparames)?getUrlParam("offset", this.urlparames):this.offset,
    pagelimit: getUrlParam("limit", this.urlparames)?getUrlParam("limit", this.urlparames):this.limit,
    load: function(callback){
        this.get_data(callback);
    },
    get_data: function(callback){
        var This = this;
        $.ajax({
            type: "get",
            url: this.searchUrl+"?search="+this.searchKey+"&limit="+this.limit+"&offset="+this.offset,
            cache: false,
            data: {},
            dataType: 'json'
        }).done(function(data){
            This.data = data;
            This.render_function(callback);

        });
    },
    generateBlogList: function(){
        var This = this;
        var blogHtml = '';
        var blogs = This.data.results;
        this.total = This.data.count;
        console.log(blogs)
        for(var i=0;i<blogs.length;i++){
            var blog = blogs[i];
            blogHtml += '<a href="/blog/blog_detail/blog_'+blog.id+'/" target=_blank>'+
                    '<div class="blog_list">'+
                        '<div class="blog_title">'+
                            '<h2>'+blog.title+''+
                            '</h2>'+
                            '<div class="blog_title_info"><div class="blog_title_info_content">'+blog.brief+'</div></div>'+
                            '<p>'+this.formatTime(blog.pub_time, 'yyyy-MM-dd HH:mm:ss')+' 阅读量:'+blog.page_views+'</p>'+
                        '</div>'+

                            '<div class="blog_img">'+
                                '<img src="'+blog.head_pic_url+'" />'+
                            '</div>'+
                    '</div>'+
                '</a>'
        }
        console.log(This.data);
        var pages =  Math.round(this.total/parseInt(this.limit));
        console.log(pages)

        blogHtml += '<ul class="pagination">';
        if (This.data.previous){
            this.offset = 0;
            blogHtml += '<li><a href="?q='+this.searchKey+'&offset='+this.offset+'">&laquo;</a></li>'
        }else{
            blogHtml += '<li class="active"><a>&laquo;</a></li>';
        }
        for(var p=1;p<pages+1;p++){
            var pageOffset = (p-1)*parseInt(this.limit);
            if (parseInt(this.pageoffset)==pageOffset){
                blogHtml += '<li class="active"><a href="?q='+this.searchKey+'&offset='+pageOffset+'">'+p+'</a></li>'
            }else{
                blogHtml += '<li><a href="?q='+this.searchKey+'&offset='+pageOffset+'">'+p+'</a></li>';
            }
        }

        $("#timeline").html(blogHtml);
    },
    resizeBlogClass: function(){
        this.blogClass.resizeClassBlogList();
    },
    render_function: function(callback){
        var This = this;
        $.each(this.funtion_name_list, function(index, value){
            This[value]();
        });
        if(callback){
            callback.call(this);
        }
    },
    formatTime: function(time, format){
        var t = new Date(time);
        var tf = function(i){return (i < 10 ? '0' : '') + i};
        return format.replace(/yyyy|MM|dd|HH|mm|ss/g, function(a){
            switch(a){
                case 'yyyy':
                    return tf(t.getFullYear());
                    break;
                case 'MM':
                    return tf(t.getMonth() + 1);
                    break;
                case 'mm':
                    return tf(t.getMinutes());
                    break;
                case 'dd':
                    return tf(t.getDate());
                    break;
                case 'HH':
                    return tf(t.getHours());
                    break;
                case 'ss':
                    return tf(t.getSeconds());
                    break;
            }
        })
    }
}

/***
*取得浏览器地址参数
*eg: home?act=all&do=none
*    getUrlParam('act') || getUrlParam('do')
*/
function getUrlParam(name, url){
    var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
    if(typeof url === 'undefined'){
        url = window.location.search.substr(1)
    }else{
        url = url.substring(url.indexOf("?")+1);
    }
    var r = url.match(reg);
    if (r!=null) return decodeURIComponent(r[2]); return null;
}

