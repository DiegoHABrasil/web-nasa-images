// document.addEventListener("DOMContentLoaded", function(){

//     let date = document.getElementById('inDate')



// })

$(document).ready(function(){

    console.log('carregou o jquery!!!');
    
    // Load of functions

    // $('#spinner-border').bind('ajaxStart', function(){
    //     $(this).show();
    // }).bind('ajaxStop', function(){
    //     $(this).hide();
    // });

    $('#btn_indate').click(getDateDois);
});


function getDate() {

    let inDate = document.getElementById('inDate').value;
    
    $.ajax({
        method: "POST",
        url: "/api-data",
        data: {
            'inDate': inDate
        },
        async: false,
        success: function(data) {
            // redirect_url("/data");
            // window.alert("data's been sent: "+data);
            if(data == 'object'){
                // usar a função .load do jQuery
            }
        }
    })

}

function getDateDois() {

    let inDate = document.getElementById('inDate').value;

    html = '<div class="spinner-border" role="status"> \
            <span class="sr-only"></span> \
            </div>'

    $('#expInfo').html(html).load(
        "/api-data",
        // Para isso funcionar, deve apontar para uma rota de POST
        //{
        //    inDate:inDate
        //},
        function(){
            console.log("load was performed");
        });

}