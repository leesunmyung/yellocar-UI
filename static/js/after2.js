
function goPage() { location.href="/"; }

$('#star_grade a').click(function(){
            System.out.println("star");
            $(this).parent().children("a").removeClass("on");  
            $(this).addClass("on").prevAll("a").addClass("on"); 
    
            return false;
});

function goStar() {
    System.out.println("goStar");
    var element = document.getElementById("starr");
            if(element.style.display == 'none'){
                    element.style.display='block'
                    element.stype.display='margin:500px';
                }
    
}

function close() {
    window.close();
}
