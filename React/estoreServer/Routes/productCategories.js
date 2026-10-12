const express = require ('express');
const productCategories = express.Router();
const mysql = require('mysql2');

const pool = mysql.createPool({
    host:"localhost",
    user:"root",
    password:"anita123",
    database: "estore",
    port:3306,
    multipleStatements: true
})

productCategories.get("/", (req,res)=>{
    let categorydata;
   
            pool.query("Select * from categories", (error, categories)=>{

                if(error){
                    categorydata = error;
                    res.status(500).send(categorydata);
                }else{
                    categorydata = categories;
                    res.status(200).send(categorydata);
                }

            })    

})



module.exports = productCategories;