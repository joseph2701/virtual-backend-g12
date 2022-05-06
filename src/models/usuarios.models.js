import mongoose from "mongoose";
import bcryptjs from "bcryptjs";

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
    
});

export const Usuario=mongoose.model("usuarios",usuarioSchema);