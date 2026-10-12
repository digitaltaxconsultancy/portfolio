const express = require ('express');
const productCategories = require('./Routes/productCategories');
const app = express();
const cors = require('cors');
const product = require('./Routes/Product');

app.use(cors());

app.use("/productCategories",productCategories)
app.use("/products", product);

const PORT = 5001;
const server = app.listen(PORT,()=>{

console.log("App is running on port 5001");

})