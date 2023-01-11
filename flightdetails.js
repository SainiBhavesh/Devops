async function fetchdetails(src,dest){
    const response = await fetch('http://127.0.0.1:8000/src=${src}&dest=${dest}');
    try{
        if(!response.ok){
            throw new Error('Failed to fetch posts : ${response.status}')
        }
        return respose.json()
    }
    catch(e){
        console.log(e);
    }
}