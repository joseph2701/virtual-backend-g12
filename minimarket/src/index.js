
import express,{json} from "express";
import {pedidosRouter} from "./routes/pedidos.routes.js";
import {productosRouter} from "./routes/productos.routes.js";
import {usuariosRouter} from "./routes/usuarios.routes.js";
import {detallePedidoRouter} from "./routes/detallePedido.routes.js";

const app=express();

app.use(json());

//nullsh coalescing operator
//si el primer valor no e snulo o undefine entonces sera ese valorm
//caso contario tomara el segundo valo
const PORT=process.env.PORT ?? 3000;

app.get("/",(req,res)=>{
    res.json({
        message:"Bienvenido a mi API del minmarket",
    });
});

//agregamos un bloque de rutas agregado en otro archivo
app.use(productosRouter);
app.use(usuariosRouter);
app.use(pedidosRouter);
app.use(detallePedidoRouter);

app.listen(PORT,() =>{
    console.log(`servidor corriendo exitosamente en el puerto  ${PORT}`);
})

//si es true pasara al segundo parametro
//ejm: si numero<50 -> sumara 1, sino no pasara
//const prueba=numero < 50  && numero+10;
//si es null o undefined no apsara
//const prueba=process.env.PORT && 10;


// const persona={
//     nombre='Joseph',
//     apellido='Mendoza'
//     //actividades:['Nadar','Montar a caballo']
// }
// // const actividades=persona.actividades && persona.actividades[0];
// let actividades=persona.actividades && persona.actividades[0];
// actividades=false;
// actividades=10.2;
// actividades = new Date();
// actividades = undefined;
// //opereador originconst numero1=0
// //en Javascript el cero significa FALSE y demas numeros TRUE
// const numero1=0;const 
// const resultado=numero1 || 10;
// const resultado2=numero2 ?? 10;
// console.log(resultado);
// console.log(resultad2);




