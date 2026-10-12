const express = require ('express');
const product = express.Router();
const mysql = require('mysql2');

const pool = mysql.createPool({
    host:"localhost",
    user:"root",
    password:"anita123",
    database: "estore",
    port:3306,
    multipleStatements: true
})

product.get("/getProducts", (req,res)=>{
    let productdata;
   
            pool.query("Select * from products", (error, products)=>{

                if(error){
                    productdata = error;
                    res.status(500).send(productdata);
                }else{
                    productdata = products;
                    res.status(200).send(productdata);
                }

            })    

})



module.exports = product;