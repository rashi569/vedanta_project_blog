function login(){
    document.getElementById("myform").style.display="flex";
}
function closeform(){
    document.getElementById("myform").style.display="none";
}

let i=0,sentence;
sentence = "Unleash Your Digital Curiosity with V-Explore Journy Through The World of Blogging";

function typingeffect(){
    if(i<sentence.length){
        document.getElementById("text").innerHTML += sentence.charAt(i);
        i++;
        setTimeout(typingeffect,50);
    }
}
typingeffect();


// function leftclick(event){
//     const leftclick = event.button;
//     if(document.getElementById("myform").style.display=="flex" && leftclick==0)
//     {
//         closeform();
//     }
//     // if(leftclick == 0 ){
//     //     prompt("clicked");
//     // }
// }

