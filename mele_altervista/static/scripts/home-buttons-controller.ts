window.onload = function () {

    function createProfile(): void {
        console.log("si");
    }

    const btnsContainer = document.getElementById("home-btns-container");

    let profile_btn = createBtn("profile", createProfile());
    let projects_btn = createBtn("projects", createProfile());
    let contacts_btn = createBtn("contacts", createProfile());
    console.log("cioan");


    console.log(btnsContainer);
}