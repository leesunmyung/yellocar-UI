
function goPage() { location.href="/"; }

$('#star_grade a').click(function(){
            $(this).parent().children("a").removeClass("on");  
            $(this).addClass("on").prevAll("a").addClass("on"); 
    
            return false;
});

function goStar() {
    
    var element = document.getElementById("starr");
            if(element.style.display == 'none'){
                    element.style.display='block';
                }
    
}

function close() {
    window.close();
}
