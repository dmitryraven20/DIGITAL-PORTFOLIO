var oneRow = '';
function multiply() {
	for (var i = 1; i < 11; i++) {
		for (var j = 1; j < 11; j++) {
			oneRow  += (j*i) + " ";       
		}
    console.log(i + " x");
    console.log(oneRow);
		oneRow = '';
	} 

}

multiply(); 