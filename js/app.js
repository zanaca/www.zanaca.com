$(document).ready(function() {
  hljs.initHighlightingOnLoad();

  if (window.location.hash != "") {
      checkHash()
  }
});


$(window).on('hashchange', function() {
    checkHash();
});

var touchMe = function(email) {
    email = email.replace(/:/g,'.')
    email = email.replace(/a/g,'c')
    email = email.replace(/\*/g,'a')
    email = email.replace(/Â¨/g,'e')
    email = email.replace(/~/g,'@')
    str = email
    email = '';
    for(i=0;i<str.length;i++) {
        email+= (i%2==0 ? str.substr(i,1) : "");
    }
    window.location = 'mailto:' + email.replace('(_)','zanaca');
}

var imgCredit = function()
{
    $(window).load("/__instagramPhoto.html", function(data) {
        var hv = $('<div/>', {
            id: 'instagram',
            title: 'Instagram photo',
            class: 'info-inserted',
            rel: 'no-follow',
            onmouseout: '$("#instagram").remove();',
            html: data
        }).appendTo('footer');

    });
}

var checkHash = function()
{
    var hash = window.location.hash.substring(1)

    if (hash == '') {
        window.location.reload();

    } else if (!isNaN(parseFloat(hash.substring(0,13))) && isFinite(hash.substring(0,13))) {
        $(window).load('/posts/' + hash, function(data){

            $("<link/>", {
                rel: "canonical",
                href: "https://medium.com/@zanaca/" + hash.substring(20).replace('.html','')
            }).appendTo("head");

            $('#container').html('<div class="posts">\
            <div class="post-summary">\
        <div class="row-fluid">'+data+'</div>\
    </div>\
    </div>');
        });
    } else {
        changeImg();
    }
}

var changeImg = function()
{
    $.ajax('/bg?hash=' + window.location.hash.substring(1)).success(function(data){
        $("<link/>", {
            rel: "stylesheet",
            type: "text/css",
            href: "/css/background.css"
        }).appendTo("head");
    });
}
