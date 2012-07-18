require(["jquery", "libs/bootstrap/tab"], function($) {
    $(function () {
        var $dialogRemove = $('.dialog-remove');

        $dialogRemove.on('click', function () {
            var option = confirm('Você deseja remover este arquivo?');

            if ( option ) {
                return true;
            } if ( !option ) {
                return false;
            }
        });

        $('.tab-content').hide();

        $('#sinopse-dashboard a').click(function ( e ) {
            var tabid = $('#sinopse-dashboard a').index( this );

            e.preventDefault();
            $( this ).tab('show');

            $('.tab-content').hide();
            $('.tab-content').eq( tabid ).show();
        });
    });
});
