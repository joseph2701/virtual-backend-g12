import {crearDetallePedidoRequestDTO} from "../dtos/detallePedido.dto.js";
import {Prisma} from '../prisma.js';

export const crearDetallePedido=async(req,res)=>{
    try{
        const data=crearDetallePedidoRequestDTO(req.body);
        //actualizar el total
        await Prisma.detallePedido.create({data});
        //para ello utiliziaremos transacciones
    await Prisma.$transaction([
        Prisma.detallePedido.create({data}),
        Prisma.pedido.update({
            data:{total:10.0},
            where:{id:data.pedidoId},
        }),
        
    ])

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