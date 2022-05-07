import validator from "validator";

export const libroRequestDTO=({nombre,avance,numPagina})=>{
    const errores=[]
    if(validator.isEmpty(nombre)){
            errores.push('Nombre no pude estar vacio')
    }
    if(avance !='COMPLETO' && avance !== 'INCOMPLETO'){
        errores.push('avance debe ser COMPLETO o INCOMPLETO')
    }
    if(avance === 'INCOMPLETO'){
        if(validator.isEmpty(numPagina.toString()) || !numPagina){
            errores.push("numPagina no puede ser vacio si el avance es INCOMPLETO");
        }
    }
    if(errores.length===0){
        throw Error(errores);        
    }else{
        return {nombre,avance,numPagina};
    }
};
