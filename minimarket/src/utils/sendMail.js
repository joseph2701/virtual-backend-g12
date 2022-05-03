import nodemailer from "nodemailer";
//                   SERVIDOR      | PUERTO
// outlook > outlook.office365.com | 587
// hotmail > smtp.live.com         | 587
// gmail >   smtp.gmail.com        | 587
// icloud >  smtp.mail.me.com      | 587
// yahoo >   smtp.mail.yahoo.com   | 587
const trasporter =nodemailer.createTransport({
    host:"smtp.gmail.com",
    auth:{
        user:process.env.EMAIL_ACCOUNT,
        pass:process.env.EMAIL_PASSWORD,
    }
});

//pagina que genera plantillas
//https://beefree.io/

export const enviarCorreoValidacion= async ({destinatario,hash})=>{
    const html=`
    <p>
        Hola para coemnzar a disfrutar de todas las ofertas de nuestro Mininarket porfavor has click en el siguiente enlace 
        <a=hef=://"www.gooogle.com">Valida mi cuenta.</a>
    </p>`;
    try{        
        await trasporter.sendMail({
            from:"joseph.mendoza.gonzales@hotmail.com",
            to:destinatario,
            subject:'Validacion de Correo de Minimarket APP',
            html,
        });
        console.log('Correo enviado exitosamentee');
    }catch(e){
        console.log(error);
        return error;
    }
};

