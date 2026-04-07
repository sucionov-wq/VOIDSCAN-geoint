async function upload(){
    let file = document.getElementById("file").files[0];
    let out = document.getElementById("output");

    if(!file){
        alert("Select file");
        return;
    }

    let form = new FormData();
    form.append("image", file);

    out.textContent = "[+] Uploading...\n";

    let res = await fetch("http://localhost:5000/analyze", {
        method: "POST",
        body: form
    });

    let data = await res.json();

    out.textContent = "";

    out.textContent += "=== EXIF DATA ===\n";
    out.textContent += JSON.stringify(data.exif, null, 2);

    out.textContent += "\n\n=== GEOINT TIPS ===\n";
    data.tips.forEach(t => {
        out.textContent += "- " + t + "\n";
    });
}