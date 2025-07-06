function submitForm() {
    const formData = new FormData();

    console.log('Name:', this.name);
    console.log('Age:', this.age);
    console.log('File:', this.file); 

    formData.append('name', this.name);
    formData.append('age', this.age);
    if (this.file && this.file.length > 0) {
        formData.append('file', this.file[0]); 
    }

    fetch('/hello', {
            method: 'POST',
            body: formData
        })
        .then(response =>{
            if(!response.ok){
                throw new Error(`HTTP error!, status: ${response.status}`);
            }
            return response.json(); 
        })
        .then(data => 
            reaction = data
        )
        .catch(error => {
            console.error('Error:', error);
    });
}