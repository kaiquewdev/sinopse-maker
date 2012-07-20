require([
    "jquery",
    "ckeditor/ckeditor", 
    "ckeditor/adapters/jquery", 
    "libs/bootstrap/tab", 
    "libs/fastFrag",
    "libs/sinopseMaker"
], function($) {
    var sinopseEditor = $('textarea.sinopse-content-editor');

    var sinopseView = $('.sinopse-content-view');

    var baseURL = SinopseMaker.slug.href();
    var slugs = SinopseMaker.slug.href;

    $(function () {

        if ( baseURL.indexOf('sinopses') > -1 ) {
            if ( baseURL.indexOf('view') > -1 ) {
                $.ajax({
                    url: '/sinopses/json/' + slugs('last'),
                    dataType: 'json',
                    success: function ( data ) {
                            sinopseView.html( SinopseMaker.html.render( data ) );    
                    }
                });
            } else if ( baseURL.indexOf('edit') > -1 ) {
                var sinopseCKEditor = sinopseEditor.ckeditor(function () {
                    var self = this;

                    $.ajax({
                        url: '/sinopses/json/' + slugs('last'),
                        dataType: 'json',
                        success: function ( data ) {
                            var renderData = SinopseMaker.html.render( data );
                            console.log( renderData );
                            //self.insertHtml( 
                            //    renderData.innerHTML    
                            //);
                        }
                    });
                });
            }
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
