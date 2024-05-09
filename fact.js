const express = require("express");

var app = express();

function factorial(n) {
    if (n === 0 || n === 1)
        return 1;
    for (var i = n - 1; i >= 1; i--) {
        n *= i;
    }
    return n;
}
app.get("/fact/:num_1", function(req, res) {
	const num1 = req.params.num_1;
	const result = factorial(num1)
	res.json({result: result});
})

app.listen(3000, function() {
	console.log("The port is 3000");
});