import mercadopago from "mercadopago";
import {Prisma} from '../prisma.js';

export const crearPreferencia= async(req,res)=>{
    
    try{
        const{pedidoId}=req.body;

        const pedidoEncontrado=await Prisma.pedido.findUnique({
            where:{id:pedidoId},
            rejectOnNotFound:true,
            include:{
                usuario:true,
                detallePedidos:{include:{producto:true}},
            },
        });
        console.log(pedidoEncontrado);
        const preferencia = await mercadopago.preferences.create({
            auto_return:'approved',
            back_urls:{
                    failure:"http://localhost:3000/pago-fallido",
                    pending:"http://localhost:3000/pago-pendiente",
                    success:"http://localhost:3000/pago-exitoso",
            },
            metadata:{
                nombre:'Prueba'
            },
            payer:{
                name: 'Joseph',
                // surname:'Mendoza',
                // address:{
                //     zip_cpde:'04002',
                //     street_name:'Calle Los Girasoles',
                //     street_number:105,                    
                // },
                email:'test_user_46542185@testuser.com',
            },
            items:pedidoEncontrado.detallePedidos.map((detallePedido)=>{
                return{
                    id:detallePedido.productoId,
                    currency_id:'PEN',
                    title:detallePedido.producto.nombre,
                    quantity:detallePedido.cantidad,
                    unit_price:detallePedido.producto.precio,                    
                };
            }),
            // [
            //     { 
            //         id:"1234",
            //         category_id:"456",
            //         currency_id:"PEN",
            //         description:'Zapatillas de Outdoor',
            //         picture_url:"https://imagenes.com",
            //         quantity:1,
            //         title:"Zapatillas edicion Otoño",
            //         unit_price:75.2,
            //     }
            // ]
        });
        
        //console.log(preferencia);

        return res.json({
            message:"Preferencia generada exitosamente",            
            content:preferencia,
        });


    }   catch (error){
        return res.json({
            message:"Error al crear la rpeferencia",
            content:error.message
        });
    }
};