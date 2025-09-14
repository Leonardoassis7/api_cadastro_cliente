# API de Empresas e Serviços.

Esta API foi desenvolvida em **Python (FastAPI)** com integração ao **MongoDB**.  
Ela permite cadastrar empresas e seus serviços associados a **municípios**, salvando login, senha e status de certificado.

---

## ⚙️ Funcionalidades.

- Criar uma empresa automaticamente ao cadastrar um serviço novo.  
- Cadastrar serviços em uma empresa, usando o **código do município** como chave.  
- Atualizar os dados de login, senha e certificado de cada município.  

### Estrutura do Documento no MongoDB
```json
{
  "_id": "123",
  "nome_empresa": "Empresa 123",
  "servicos": {
    "3550308": {
      "login": "usuario123",
      "senha": "senha123",
      "certificado": true
    }
  }
}
