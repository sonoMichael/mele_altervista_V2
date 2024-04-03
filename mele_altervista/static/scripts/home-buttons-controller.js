window.onload = function () {
    function createBtn(name, fn) {
        var res = document.createElement("div");
        res.classList.add("home-button", "pe-6", "text-end");
        var temp = document.createElement("div");
        temp.classList.add("on-hover");
        temp.addEventListener("click", fn);
        var text = document.createElement("span");
        text.textContent = name;
        res.appendChild(temp);
        res.appendChild(text);
        btnsContainer === null || btnsContainer === void 0 ? void 0 : btnsContainer.appendChild(res);
    }
    function createProfile() {
        console.log("si");
    }
    var btnsContainer = document.getElementById("home-btns-container");
    var profile_btn = createBtn("profile", createProfile());
    var projects_btn = createBtn("projects", createProfile());
    var contacts_btn = createBtn("contacts", createProfile());
    console.log("cioan");
    console.log(btnsContainer);
};
