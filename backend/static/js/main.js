/*
 * ELT Pages
 * Dr. Gurvan M. F. Bazin
 */

let scrollMonitor = () => {

    const navHeight = $(window).height() - 70;
    const navHeightDirection = $(window).height() - 300;
    // console.log('DEBUG', $('#big-header').offset().top, $('#big-header').height(), $(window).scrollTop(), navHeight);
    if (($('#big-header').offset().top + $('#big-header').height() < $(window).scrollTop() + navHeight)) {
        $('#main-navbar').addClass('mysticky').removeClass('myfixed');
    }
    else {
        $('#main-navbar').removeClass('mysticky').addClass('myfixed');
    }
    if (($('#big-header').offset().top + $('#big-header').height() < $(window).scrollTop() + navHeightDirection)) {
        $('.dropup.dropdown-menu-top').removeClass('dropup').addClass('dropdown');
        $('.dropdown-submenu > .dropdown-menu').removeClass('bottom-aligned').addClass('top-aligned');
    }
    else {
        $('.dropdown.dropdown-menu-top').removeClass('dropdown').addClass('dropup');
        $('.dropdown-submenu > .dropdown-menu').removeClass('top-aligned').addClass('bottom-aligned');
    }

    document.querySelector('.big-header-image').style.transform = `translate(0, ${- 0.5 * $(window).scrollTop()}px)`;
}

$( window ).on( "load", function() {
    scrollMonitor();
});

$( document ).ready(function() {

    // AOS.init();

    $(window).resize(scrollMonitor);
    $(window).bind('scroll', scrollMonitor);

    $('.share-social-media-link').each(function(index, element) {
        // console.log($(this), $(this).attr('href'));
        let href = $(this).attr('href');
        href = href.replace('https://elt.eso.org/', window.location.href);
        $(this).attr('href', href);
    });

  $('.share-email').on('click', function (event) {
    event.preventDefault();
    var email = '';
    var subject = $(document).attr('title');
    var emailBody = window.location.href;
    window.location = 'mailto:' + email + '?subject=' + subject + '&body=' +   emailBody;
  });

  $('.share-facebook').on('click', function (event) {
    event.preventDefault();
    const newLocation = 'https://www.facebook.com/sharer/sharer.php?u=' + window.location.href;
    // console.log('DEBUG', newLocation);
    window.location = newLocation;
  });

  $('.share-twitter').on('click', function (event) {
    event.preventDefault();
    const newLocation = 'https://twitter.com/intent/tweet?url=' + window.location.href + '&text=&via=ESO';
    // console.log('DEBUG', newLocation);
    window.location = newLocation;
  });

  $('.clipboard').on('click', function(event) {
    event.preventDefault();
    var $temp = $("<input>");
    var $url = $(location).attr('href');
    $("body").append($temp);
    $temp.val($url).select();
    document.execCommand("copy");
    $temp.remove();
  })

  $("div.dropdown-menu [data-toggle='dropdown']").on("click", function(event) {
    event.preventDefault();
    event.stopPropagation();
    
    //method 1: remove show from sibilings and their children under your first parent
    
/* 		if (!$(this).next().hasClass('show')) {
		      
		        $(this).parents('.dropdown-menu').first().find('.show').removeClass('show');
		     }  */     
     
    //method 2: remove show from all siblings of all your parents
    $(this).parents('.dropdown-submenu').siblings().find('.show').removeClass("show");
   
    $(this).siblings().toggleClass("show");
    
    //collapse all after nav is closed
    $(this).parents('li.nav-item.dropdown.show').on('hidden.bs.dropdown', function(e) {
      $('.dropdown-submenu .show').removeClass("show");
    });

  });

    /* For changing color of polygon and text on hover
    */

    const esoblue = 'rgb(0, 119, 190)';
    const deg = Math.PI / 180;

    const uint8 = (value) => {
        return 0 > value ? 0 : (255 < value ? 255 : Math.round(value));
    };

    const changeColor = (color) => {

        const c = color.replace('rgb(', '').replace(')', '').replace(' ', '').split(',');
        // console.log('DEBUG', c);
        const r = c[0];
        const g = c[1];
        const b = c[2];

        const hue = 180;
        const cosA = Math.cos(hue * deg);
        const sinA = Math.sin(hue * deg);
        const neo = [
          cosA + (1 - cosA) / 3,
          (1 - cosA) / 3 - Math.sqrt(1 / 3) * sinA,
          (1 - cosA) / 3 + Math.sqrt(1 / 3) * sinA,
        ];
        let result = [
          r * neo[0] + g * neo[1] + b * neo[2],
          r * neo[2] + g * neo[0] + b * neo[1],
          r * neo[1] + g * neo[2] + b * neo[0],
        ];
        result = result.map(x => uint8(x));
        return 'rgb(' + result[0] + ', ' + result[1] + ', ' + result[2] + ')';
    };

    let textColor = null;
    let fillColor = null;

    $('svg.internal-menu-trapezoid > a > polygon').hover(
        (event) => {
            let column = $(event.target).parent().parent().parent().parent().parent();
            // console.log('DEBUG', column);
            let textlink = column.children('.internal-menu-trapezoid-link').children('a');
            // console.log('DEBUG', textlink.css('color'));
            textColor = textlink.css('color');
            fillColor = $(event.target).css('fill');
            // console.log('DEBUG', $(event.target).css('fill'));
            textlink.css('color', fillColor);
            let changedColor = esoblue;
            // let changedColor = changeColor(textColor);
            // if (changedColor === textColor) {
            //     changedColor = 'rgb(154, 111, 94)';
            // }
            // console.log('DEBUG', changedColor);
            $(event.target).css('fill', changedColor);
        },
        (event) => {
            let column = $(event.target).parent().parent().parent().parent().parent();
            let textlink = column.children('.internal-menu-link').children('a');
            textlink.css('color', textColor);
            $(event.target).css('fill', fillColor);
        }
    );

    $('svg.internal-menu-trapezoid > a > polygon').click(
        (event) => {
            let column = $(event.target).parent().parent().parent().parent().parent();
            let textlink = column.children('.internal-menu-link').children('a');
            textlink.css('color', textColor);
            $(event.target).css('fill', fillColor);
        }
    );

});

