```javascript
comandos → comando comandos  
         | comando  

comando → USAR ORBE EM lista_uuid  
        | CRIAR lista_itens  
        | LISTAR lista_itens  
        | LISTAR TODOS  
        | LISTAR UUID  

lista_itens → ITEM lista_itens_aux  
            | UUID lista_itens_aux  

lista_itens_aux → VIRGULA ITEM lista_itens_aux  
                | VIRGULA UUID lista_itens_aux  
                | vazio  

lista_uuid → UUID lista_uuid_aux  

lista_uuid_aux → VIRGULA UUID lista_uuid_aux  
               | vazio  

vazio → ε  
```