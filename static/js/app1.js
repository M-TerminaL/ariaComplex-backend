// writing automatically in slider header box //

let string = "مجموعه ورزشی آریا";
let str = document.getElementById("str");
let split = string.split("");


(function anim(){
    let running = setTimeout(anim, 100);
    split.length > 0 ? str.innerHTML += split.shift(): clearTimeout(running);
})();

// end writing automatically in slider header box //