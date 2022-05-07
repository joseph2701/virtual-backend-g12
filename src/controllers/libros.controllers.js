import {libroRequestDTO} from "../dtos/libro.request.dto.js";
import { Usuario } from "../models/usuarios.models.js";

export const agregarLibro= async (req,res) =>{
    try{
        const data=req.body;
        console.log(req.user);
        const usuarioActual=req.user;
        usuarioActual.libros.push(data);
        //itnernamente cuando hacemos busqueda en mongoose, se jala algunos datos para poder 
        // sobreescribir o modificar ese reistro a nivel de db, esto es asincrono
        await usuarioActual.save();

        return res.json({
            message:"ok",
            content:usuarioActual.libros,
        });
    }catch(e){
        return res.json({
           message:"Error al agregar el libro",
           content:e.message,
        });
    }
};

export const listarLibros = (req,res)=>{
    //req.user < toda la data de nuestro usuario
    
    return res.json({
        message:"Los libros son:",
        content: req.user.libros,
    });
};


//http://localhost:3000/libro/:id
export const devolverLibro = async (req,res)=>{
    const {_id: id_del_libro}=req.params;
    console.log(id_del_libro);
    // const {_id2}=req.params.libros._id;
    
    const libroEncontrado= await Usuario.findOne({
        _id:req.user._id,
        'libros._id':id_del_libro,
    },
    {
        "libros.$":1,
    }
    );

    // https://www.mongodb.com/docs/manual/reference/operator/projection/positional/#proj._S_
    // console.log(req.user.libros);
    const libroEncontrado2= req.user.libros.filter((libro)=>{
        console.log(libro._id);
        return libro._id.toString()===id_del_libro})


    return res.json({
        message:"El libro es:",
        content: libroEncontrado,
        content2: libroEncontrado2,
    });
};