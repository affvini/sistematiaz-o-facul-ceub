#Total de vendas dos vendedores
Emily = float(input('Insira os valores de venda da vendedora Emily: '))
Larissa = float(input('Insira os valores de venda da vendedora Larissa: '))
Rafael = float(input('Insira os valores de venda do vendedor Rafael: '))
Milena = float(input('Insira os valores de venda da vendedora Milena: '))

#Salário fixo
salario_fixo_vendedor = 1000
salario_fixo_gerente = 2000


if Emily and Larissa and Rafael and Milena < 5000:
    total_emily = Emily * 0.01 + salario_fixo_vendedor
    total_larissa = Larissa * 0.01 + salario_fixo_vendedor
    total_rafael = Rafael * 0.01 + salario_fixo_vendedor
    total_milena = Milena * 0.01 + salario_fixo_vendedor

    print('Salário da Emily (Vendedora) = R$', total_emily)
    print('Salário da Larissa (Vendedora) = R$', total_larissa)
    print('Salário do Rafael (Vendedor) = R$', total_rafael)
    print('Salário da Milena (Vendedora) = R$', total_milena)

elif Emily and Larissa and Rafael and Milena > 5000 and Emily and Larissa and Rafael and Milena < 10000:
    total_emily = Emily * 0.015 + salario_fixo_vendedor
    total_larissa = Larissa * 0.015 + salario_fixo_vendedor
    total_rafael = Rafael * 0.015 + salario_fixo_vendedor
    total_milena = Milena * 0.015 + salario_fixo_vendedor

    print('Salário da Emily (Vendedora) = R$', total_emily)
    print('Salário da Larissa (Vendedora) = R$', total_larissa)
    print('Salário do Rafael (Vendedor) = R$', total_rafael)
    print('Salário da Milena (Vendedora) = R$', total_milena)

else:
    total_emily = Emily * 0.2 + salario_fixo_vendedor
    total_larissa = Larissa * 0.2 + salario_fixo_vendedor
    total_rafael = Rafael * 0.2 + salario_fixo_vendedor
    total_milena = Milena * 0.2 + salario_fixo_vendedor

    print('Salário da Emily (Vendedora) = R$', total_emily)
    print('Salário da Larissa (Vendedora) = R$', total_larissa)
    print('Salário do Rafael (Vendedor) = R$', total_rafael)
    print('Salário da Milena (Vendedora) = R$', total_milena)

faturamento_total_vendedores = Emily + Larissa + Rafael + Milena
comissao_gerente = (faturamento_total_vendedores * 0.05) + salario_fixo_gerente


total_salarios = float(total_emily) + float(total_larissa) + float(total_milena) + float(total_rafael) + float(comissao_gerente)
print('Salário da Jéssica (gerente) = R$', comissao_gerente)
print('Total dos salários = ', total_salarios)
