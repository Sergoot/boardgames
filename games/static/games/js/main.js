const postForm = document.querySelector("#form");


function handleSubmit(postForm) {
    postForm.addEventListener("submit", e => {
        e.preventDefault();
        formData = new FormData(postForm);
        fetch('/create/', {
                method: 'POST',
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                postForm.reset();

            })
            .catch((error) => {
                console.error('Error:', error);
            });
    })
}

handleSubmit(postForm)
console.log(data)