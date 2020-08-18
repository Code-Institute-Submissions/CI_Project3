$(document).ready(function () {
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();
    $('.carousel').carousel();
    $('select').formSelect();
});


$(window).resize(function () {
    if ($(window).width() <= 1024) {
        $('#singlecard').removeClass('horizontal large');
    }
});