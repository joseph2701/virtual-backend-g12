import express from "express";
import morgan from "morgan";
import mongoose from "mongoose";
import {usuarioRouter} from "./routes/usuarios.routes.js";

const app=express();
// const logger=morgan("combined");
const logger=morgan("dev");
//const logger=morgan("common");

app.use(logger);
app.use(express.json())
app.use(usuarioRouter)
const PORT=process.env.PORT ?? 3000;

mongoose
    .connect(process.env.MONGO_URL)
    .then((valor)=>{
        console.log("Conectado a la db ")
    })
    .catch((error)=>{
        console.log(error)
        console.log("Conectado a la db ")
    });
    

app.listen(PORT,()=>{
    console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
