import{Prisma} from "../prisma.js";

export const crearProducto=async (req,res)=>{
    console.log("yo me ejecuto primero");
    try{
        const resultado= await Prisma.producto.create({data:req.body})
        console.log(resultado);

        return res.json({
            message:"Producto agregado exitosamente",
        });       
    }catch(e){
        console.log(e);
        return res.json({
            message:"Error al crear el producto",
        });
    }    
};

export const listarProductos = async(req,res)=>{
    const productos = await Prisma.producto.findMany({});
    const resultado= await Prisma.producto.create({data:req.body})
    return res.json({
        content:productos,
    });
};

export const actualizarProductos = async(req,res)=>{
    try{
        const id= req.params.id
        //si queremos ahcer filtro por columna que nos ea unique
        //findFirst()
        const productoEncontrado = await Prisma.producto.findUnique({where: {id:+id}});
        console.log(productoEncontrado)
        const productoActualizado = await Prisma.producto.update({
            data:req.body,
            where:{id:+id},
        })
        return res.json({
            message:"Producto actualizado con exito",
            content:productoActualizado,
        });        
    }catch(e){
        console.log(e);
        return res.json({
            message:"Error al actualizar el producto",
        });
    }    
};


export const eliminarProductos = async(req,res)=>{
    try{
        const id= req.params.id
        const productoEncontrado = await Prisma.producto.findUnique({
            where: {id:+id},
            select:{id:true},
        });

        console.log(productoEncontrado)
        
        const productoEliminado = await Prisma.producto.delete({where:{id:+id}});
        return res.json({
            message:"Producto eliminado con exito",
            content:productoEliminado,
        });        
    }catch(e){
        console.log(e);
        return res.json({
            message:"Error al eliminar el producto",
        });
    }    
};

