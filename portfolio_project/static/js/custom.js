/*global jQuery:false */
jQuery(document).ready(function ($) {
  "use strict";


  //add some elements with animate effect

  $(".big-cta").hover(
    function () {
      $('.cta a').addClass("animated shake");
    },
    function () {
      $('.cta a').removeClass("animated shake");
    }
  );
  $(".box").hover(
    function () {
      $(this).find('.icon').addClass("animated fadeInDown");
      $(this).find('p').addClass("animated fadeInUp");
    },
    function () {
      $(this).find('.icon').removeClass("animated fadeInDown");
      $(this).find('p').removeClass("animated fadeInUp");
    }
  );


  $('.accordion').on('show', function (e) {

    $(e.target).prev('.accordion-heading').find('.accordion-toggle').addClass('active');
    $(e.target).prev('.accordion-heading').find('.accordion-toggle i').removeClass('icon-plus');
    $(e.target).prev('.accordion-heading').find('.accordion-toggle i').addClass('icon-minus');
  });

  $('.accordion').on('hide', function (e) {
    $(this).find('.accordion-toggle').not($(e.target)).removeClass('active');
    $(this).find('.accordion-toggle i').not($(e.target)).removeClass('icon-minus');
    $(this).find('.accordion-toggle i').not($(e.target)).addClass('icon-plus');
  });


  // tooltip
  $('.social-network li a, .options_box .color a').tooltip();

  //scroll to top
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $('.scrollup').fadeIn();
    } else {
      $('.scrollup').fadeOut();
    }
  });
  $('.scrollup').click(function () {
    $("html, body").animate({ scrollTop: 0 }, 1000);
    return false;
  });
  $('#post-slider').flexslider({
    // Primary Controls
    controlNav: true,              //Boolean: Create navigation for paging control of each clide? Note: Leave true for manualControls usage
    directionNav: true,              //Boolean: Create navigation for previous/next navigation? (true/false)
    prevText: "Previous",        //String: Set the text for the "previous" directionNav item
    nextText: "Next",            //String: Set the text for the "next" directionNav item

    // Secondary Navigation
    keyboard: true,              //Boolean: Allow slider navigating via keyboard left/right keys
    multipleKeyboard: false,             //{NEW} Boolean: Allow keyboard navigation to affect multiple sliders. Default behavior cuts out keyboard navigation with more than one slider present.
    mousewheel: false,             //{UPDATED} Boolean: Requires jquery.mousewheel.js (https://github.com/brandonaaron/jquery-mousewheel) - Allows slider navigating via mousewheel
    pausePlay: false,             //Boolean: Create pause/play dynamic element
    pauseText: 'Pause',           //String: Set the text for the "pause" pausePlay item
    playText: 'Play',            //String: Set the text for the "play" pausePlay item

    // Special properties
    controlsContainer: "",                //{UPDATED} Selector: USE CLASS SELECTOR. Declare which container the navigation elements should be appended too. Default container is the FlexSlider element. Example use would be ".flexslider-container". Property is ignored if given element is not found.
    manualControls: "",                //Selector: Declare custom control navigation. Examples would be ".flex-control-nav li" or "#tabs-nav li img", etc. The number of elements in your controlNav should match the number of slides/tabs.
    sync: "",                //{NEW} Selector: Mirror the actions performed on this slider with another slider. Use with care.
    asNavFor: "",                //{NEW} Selector: Internal property exposed for turning the slider into a thumbnail navigation for another slider
  });

  $('#main-slider').flexslider({
    namespace: "flex-",           //{NEW} String: Prefix string attached to the class of every element generated by the plugin
    selector: ".slides > li",    //{NEW} Selector: Must match a simple pattern. '{container} > {slide}' -- Ignore pattern at your own peril
    animation: "fade",            //String: Select your animation type, "fade" or "slide"
    easing: "swing",           //{NEW} String: Determines the easing method used in jQuery transitions. jQuery easing plugin is supported!
    direction: "horizontal",      //String: Select the sliding direction, "horizontal" or "vertical"
    reverse: false,             //{NEW} Boolean: Reverse the animation direction
    animationLoop: true,              //Boolean: Should the animation loop? If false, directionNav will received "disable" classes at either end
    smoothHeight: false,             //{NEW} Boolean: Allow height of the slider to animate smoothly in horizontal mode
    startAt: 0,                 //Integer: The slide that the slider should start on. Array notation (0 = first slide)
    slideshow: true,              //Boolean: Animate slider automatically
    slideshowSpeed: 7000,              //Integer: Set the speed of the slideshow cycling, in milliseconds
    animationSpeed: 600,               //Integer: Set the speed of animations, in milliseconds
    initDelay: 0,                 //{NEW} Integer: Set an initialization delay, in milliseconds
    randomize: false,             //Boolean: Randomize slide order

    // Usability features
    pauseOnAction: true,              //Boolean: Pause the slideshow when interacting with control elements, highly recommended.
    pauseOnHover: false,             //Boolean: Pause the slideshow when hovering over slider, then resume when no longer hovering
    useCSS: true,              //{NEW} Boolean: Slider will use CSS3 transitions if available
    touch: true,              //{NEW} Boolean: Allow touch swipe navigation of the slider on touch-enabled devices
    video: false,             //{NEW} Boolean: If using video in the slider, will prevent CSS3 3D Transforms to avoid graphical glitches

    // Primary Controls
    controlNav: true,              //Boolean: Create navigation for paging control of each clide? Note: Leave true for manualControls usage
    directionNav: true,              //Boolean: Create navigation for previous/next navigation? (true/false)
    prevText: "Previous",        //String: Set the text for the "previous" directionNav item
    nextText: "Next",            //String: Set the text for the "next" directionNav item

    // Secondary Navigation
    keyboard: true,              //Boolean: Allow slider navigating via keyboard left/right keys
    multipleKeyboard: false,             //{NEW} Boolean: Allow keyboard navigation to affect multiple sliders. Default behavior cuts out keyboard navigation with more than one slider present.
    mousewheel: false,             //{UPDATED} Boolean: Requires jquery.mousewheel.js (https://github.com/brandonaaron/jquery-mousewheel) - Allows slider navigating via mousewheel
    pausePlay: false,             //Boolean: Create pause/play dynamic element
    pauseText: 'Pause',           //String: Set the text for the "pause" pausePlay item
    playText: 'Play',            //String: Set the text for the "play" pausePlay item

    // Special properties
    controlsContainer: "",                //{UPDATED} Selector: USE CLASS SELECTOR. Declare which container the navigation elements should be appended too. Default container is the FlexSlider element. Example use would be ".flexslider-container". Property is ignored if given element is not found.
    manualControls: "",                //Selector: Declare custom control navigation. Examples would be ".flex-control-nav li" or "#tabs-nav li img", etc. The number of elements in your controlNav should match the number of slides/tabs.
    sync: "",                //{NEW} Selector: Mirror the actions performed on this slider with another slider. Use with care.
    asNavFor: "",                //{NEW} Selector: Internal property exposed for turning the slider into a thumbnail navigation for another slider
  });
  /* -------- Isotope Filtering -------- */
  var $container = $('#isotope-gallery-container');
  var $filter = $('.filter');
  $(window).load(function () {
    // Initialize Isotope
    $container.isotope({
      itemSelector: '.gallery-item-wrapper'
    });
    $('.filter a').click(function () {
      var selector = $(this).attr('data-filter');
      $container.isotope({ filter: selector });
      return false;
    });
    $filter.find('a').click(function () {
      var selector = $(this).attr('data-filter');
      $filter.find('a').parent().removeClass('active');
      $(this).parent().addClass('active');
    });
  });
  $(window).smartresize(function () {
    $container.isotope('reLayout');
  });
  // End Isotope Filtering
  $('.gallery-zoom').magnificPopup({
    type: 'image'
    // other options
  });

});

/* text project ref : https://gahyun-web-diary.tistory.com/2 */
var typingBool = false;
var typingIdx = 0;
var liIndex = 0;
var liLength = $(".typing-txt>ul>li").length;

// 타이핑될 텍스트를 가져온다 
var typingTxt = $(".typing-txt>ul>li").eq(liIndex).text();
typingTxt = typingTxt.split(""); // 한글자씩 자른다. 
if (typingBool == false) { // 타이핑이 진행되지 않았다면 
  typingBool = true;
  var tyInt = setInterval(typing, 100); // 반복동작 
}

function typing() {
  if (typingIdx < typingTxt.length) { // 타이핑될 텍스트 길이만큼 반복 
    $(".typing").append(typingTxt[typingIdx]); // 한글자씩 이어준다. 
    typingIdx++;
  } else { //한문장이끝나면
    //다음문장으로.. 마지막문장이면 다시 첫번째 문장으로 
    if (liIndex >= liLength - 1) {
      liIndex = 0;
    } else {
      liIndex++;
    }

    //다음문장을 타이핑하기위한 셋팅
    typingIdx = 0;
    typingBool = false;
    typingTxt = $(".typing-txt>ul>li").eq(liIndex).text();

    //다음문장 타이핑전 1초 쉰다
    clearInterval(tyInt);
    setTimeout(function () {
      $(".typing").html('');
      tyInt = setInterval(typing, 100);
    }, 1000);
  }
}

// User signup 부가 기능 구현
function idCheck() {
  if (!$('#username').val()) {
    alert("ID를 입력해 주시기 바랍니다.");
    return;
  }

  $.ajax({
    type: "POST",
    url: "/user/signup_idcheck/",
    data: {
      'username': $('#username').val(),
      'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
    },
    success: function (response) {
      $('#idcheck-result').html(response);
    },
  });
}

function changeEmailDomain() {
  $('#email_domain').val($('#email_selection').val());
}

function cancelUserRegister() {
  var result = confirm("회원가입을 취소하시겠습니까?");

  if (result) {
    $(location).attr('href', '/user/login');
  }
}

function userRegister() {
  if (!$('#username').val()) {
    alert("아이디를 입력해 주시기 바랍니다.");
    return;
  }
  if (!$('#IDCheckResult').val()) {
    alert("ID 중복체크를 먼저 진행해 주시기 바랍니다.");
    return;
  }
  if (!$('#password').val()) {
    alert("비밀번호를 입력해 주시기 바랍니다.");
    return;
  }
  if ($('#password').val().length < 8) {
    alert('비밀번호는 최소 8자 이상이여야 합니다.');
    alert($('#password').val().length);
    return;
  }
  if ($('#password').val() != $('#password_check').val()) {
    alert("비밀번호가 일치하지 않습니다.");
    return;
  }
  if (!$('#name').val()) {
    alert("이름을 입력해 주시기 바랍니다.");
    return;
  }


  // if (!$('#email').val()) {
  //   alert("E-mail 주소를 올바르게 입력해 주시기 바랍니다.");
  //   return;
  // }

  $('#register_form').submit();
}

function changePassword() {
  if (!$('#id_old_password').val()) {
    alert("비밀번호를 입력해 주시기 바랍니다.");
    return;
  }
  if ($('#id_new_password1').val() != $('#id_new_password2').val()) {
    alert("비밀번호가 일치하지 않습니다.");
    return;
  }
  $('#mypage_form').submit();
}



$(document).ready(function() {
	$('input').keydown(function(e) {
		if (e.which == 13)
		{
			$('form').submit();
		}
	});
});

function login() {
	if (!$('#username').val())
	{
		alert("아이디를 입력해 주시기 바랍니다");
		return;
	}
	if (!$('#password').val()) {
		alert("비밀번호를 입력해 주시기 바랍니다");
		return;
	}

	$('#login_form').submit();
}

