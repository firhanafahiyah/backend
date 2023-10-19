// menangkap semua elemen a
document.querySelectorAll("#opts a").forEach((a) =>
    // jika di klik akan menjalankan fungsi computerchoice
    a.addEventListener("click", (element) => {
        computerChoice(element);
    })

);
function computerChoice(element) {
    //tangkap pilihan user
    let pilihanuser = element.target.innerText;

    // menangkap elemen result dengan queryselector untuk menampung
    // nilai hasil dari game
    let pilihanComputer = document.querySelector("#result");

    // membuat array pilihan untuk komputer
    let choices = ["Rock", "Paper", "Scissors"];

    // pilihan rando m untuk komputer
    pilihanComputer.innerHTML =
    choices[Math.round(Math.random() * choices.length)];
    pilihanComputer = pilihanComputer.innerHTML;

    // jika pilihan komputer dan pilihan user sama (draw)
    if (pilihanuser == pilihanComputer) {
        alert("DRAW");
    }

    //jika pilihan user yang  menang
    if (pilihanuser == "Rock" && pilihanComputer == "Scissors") {
        alert("YOU WIN");
    }else if (pilihanuser == "Paper" && pilihanComputer == "Rock"){
        alert("YOU WIN");
    }else if (pilihanuser == "Scissors" && pilihanComputer == "Paper"){
        alert("YOU WIN");
    }

}   

    // jika pilihan komputer menang
    if (pilihanuser == "Rock" && pilihanComputer == "Paper") {
        alert("YOU LOSE");
    }else if (pilihanuser == "Paper" && pilihanComputer== "Scissors"){
        alert("YOU LOSE");
    }else if (pilihanuser == "Scissors" && pilihanComputer == "Paper"){
        alert("YOU LOSE");
    }