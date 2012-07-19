require([
    "jquery", 
    "libs/bootstrap/tab", 
    "libs/fastFrag",
    "libs/sinopseMaker"
], function($) {

    $(function () {
        var sinopseView = $('.sinopse-content-view');
        var baseURL = SinopseMaker.slug.href();
        var slugs = SinopseMaker.slug.href;

        if ( 
            baseURL.indexOf('sinopses') > -1 &&
            baseURL.indexOf('view') > -1
        ) {
            // For render content

            $.ajax({
                url: '/sinopses/json/' + slugs('last'),
                dataType: 'json',
                success: function ( data ) {
                    sinopseView.html( SinopseMaker.html.render( data ) );    
                }
            });
        } if ( slugs('last') === 'sinopses' ) {
            // For tabs

            $('.tab-content').hide().eq(1).show();

            $('#sinopse-dashboard a').click(function ( e ) {
                var tabid = $('#sinopse-dashboard a').index( this );

                e.preventDefault();
                $( this ).tab('show');

                $('.tab-content').hide();
                $('.tab-content').eq( tabid ).show();
            });
        }
    });
});
