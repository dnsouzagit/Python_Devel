from pylogix import PLC

# Substitua '192.168.1.10' pelo endereço IP do seu CLP
ip_address = '192.168.1.10'

# Cria uma instância do objeto PLC e conecta ao CLP
with PLC() as plc:
    plc.IPAddress = ip_address
    
    # Substitua 'TagName' pelo nome da tag que você deseja ler
    tag_name = 'TagName'
    
    # Lê o valor da tag
    result = plc.Read(tag_name)
    
    # Verifica se a leitura foi bem-sucedida
    if result.Status == 'Success':
        print(f'O valor da tag {tag_name} é: {result.Value}')
    else:
        print(f'Erro ao ler a tag {tag_name}: {result.Status}')
