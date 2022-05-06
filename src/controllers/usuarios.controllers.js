import {Usuario} from '../models/usuarios.models.js';
import bcryptjs from "bcryptjs";

export const registrarUsuario=async (req,res)=>{   
        const data=req.body
        try{
            const nuevoUsuario=await Usuario.create(data);

            console.log(nuevoUsuario.toJSON());
            console.log(Object.keys(nuevoUsuario));

            //Forma 1 de eliminar un atributo del JSON
            const result=nuevoUsuario.toJSON();
            delete result["password"];

            //forma 2 de eliminar un atributo del JSON
            delete nuevoUsuario["_doc"]["password"];

            return res.status(201).json({
                message:"Usuario crado exitosamente",
                content:nuevoUsuario, //result,
            });
        }catch(e){
            return res.status(400).json({
                message: "Error al crear el usuario",
                content: e.message,
            });
        }        
};


export const   login = async (req,res)=>{
    //validar que se envie la pwd y el correo
    const data=req.body
    //primero busco el usuaro en la bd
    const usuarioEncontrado=await Usuario.findOne({correo: data.correo})

    if (!usuarioEncontrado){
        return res.status(400).json({
            message:'Credenciales incorrectas'
        })
    }
    
    //valida su pwd
    if (bcryptjs.compareSync(data.password,usuarioEncontrado.password)){
        return res .json({
            message:"Bienvenidos",
        });
    }else{
        return res.status(400).json({
            message:"Credenciales incorrectas",
        });
    }
};