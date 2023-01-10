function getInput() {
    var form = document.getElementById("form");
    var source = form.elements.source.value;
    var destination = form.elements.destination.value;
    console.log(destination);
    // Perform actions based on the user's input, such as displaying a message to the user or making an AJAX request.
    document.getElementById("src").innerHTML =source;
    document.getElementById("dst").innerHTML =destination;


    const srcobject = {
      src: source
    };
    const dstobject = {
      dst: destination
    };

     jsonString1 = JSON.stringify(srcobject);
     jsonString2 = JSON.stringify(dstobject);

    console.log(jsonString1);
    console.log(jsonString2);

  }


  getInput()