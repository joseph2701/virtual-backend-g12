import {crearDetallePedidoRequestDTO} from "../dtos/detallePedido.dto.js";
import {Prisma} from '../prisma.js';

export const crearDetallePedido=async(req,res)=>{
    try{    
        const data=crearDetallePedidoRequestDTO(req.body);
        await Prisma.$transaction(async () =>{
            
            //hago la busqueda del producto
            const {precio}=await Prisma.producto.findUnique({
                where:{id:data.pedidoId},
                rejectOnNotFound:false,
                select:{precio:true},
            });
            
            //hago la busqueda del pedido
            const {id,total}=await Prisma.pedido.findUnique({
                where:{id:data.pedidoId},
                rejectOnNotFound:true,
                select:{id:true,total:true},
            });
            
            //crea el detalle de ese pedido con la modificacion del subtotal
            const {subTotal}=await Prisma.detallePedido.create({
                data:{...data,subTotal:precio*data.cantidad},                
                select:{subTotal:true},
            });
            
            //actualizo ahora el total del pedido
            await Prisma.pedido.update({
                data:{total:total+subTotal},                
                where:{id},
            });            
        });

        return res.status(201).json({
            message:"Detalle creado exitosamente",            
        });

    }catch(error){
        return res.status(400).json({
            message:"Error al crear el detalle del epdido",
            content:error.message,
        });
    }
};