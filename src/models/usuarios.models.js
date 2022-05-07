import mongoose from "mongoose";
import bcryptjs from "bcryptjs";

const libroSchema=new mongoose.Schema(
    {
        nombre:{
            type:mongoose.Schema.Types.String,
            required:true,        
        }, 
        avance: {
            type: String,
            enum : ['COMPLETO','INCOMPLETO'],
            default: 'COMPLETO',
            required:true,
        },
        numPagina:{
            type:mongoose.Schema.Types.Number,
            min:1,
            name:'num_pagina', //en la db la columna se llama num_pagina mientras que en mongoose se llamara numPagina
        },
    },
    {
        // _id:false,
        timestamps:{
            updateAt: "fecha_actualizacion", //creara la columna con ese nombbre
        },//dentro de timestamps, se deben crear las columnas de auditoria creeated_At y el updated_at
    }
);




const usuarioSchema= new mongoose.Schema({
    correo:{
        type: mongoose.Schema.Types.String,
        required:true,
        unique:true,
         // ademas de las configuraciones generales tenemos algunas configuraciones dependiendo del tipo de dato
        // https://mongoosejs.com/docs/schematypes.html
        lowercase: true,
        maxlength: 100,
    },
    nombre:mongoose.Schema.Types.String,     //aca no se ´podra modificar
    
    telefono:{
        type:mongoose.Schema.Types.Number,
        required:false,
    },
    // password: {
    //     type: mongoose.Schema.Types.String,
    //     set: (valorActual) => {
    //       console.log(valorActual);
    //       return valorActual;
    //     },
    // }
    password:{
        type:mongoose.Schema.Types.String,
        set:(valorActual)=> bcryptjs.hashSync(valorActual,10),        
            // return "hola";   
            // get:(valorActual)=>null,            
    },



    //si la relacion feura 1:1
    // libro:libroSchema
    
    //la relacion de 1:n un usuario puede tener varios libros
    libros:{
        type:[libroSchema],
    },
    
});

export const Usuario=mongoose.model("usuarios",usuarioSchema);