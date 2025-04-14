function uploadImage() {
    const input = document.getElementById('imageInput');
    const file = input.files[0];
    if (!file) return alert('Please select an image');

    const formData = new FormData();
    formData.append('image', file);

    fetch('https://rembg-1.onrender.com', {
        method: 'POST',
        body: formData
    })
    .then(res => res.blob())
    .then(blob => {
        const url = URL.createObjectURL(blob);
        const outputImage = document.getElementById('outputImage');
        const downloadLink = document.getElementById('downloadLink');
        outputImage.src = url;
        outputImage.style.display = 'block';
        downloadLink.href = url;
        downloadLink.style.display = 'inline';
    })
    .catch(err => alert('Error: ' + err));
}
