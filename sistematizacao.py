#Total de vendas dos vendedores
Emily = float(input('Insira os valores de venda da vendedora Emily: '))
Larissa = float(input('Insira os valores de venda da vendedora Larissa: '))
Rafael = float(input('Insira os valores de venda do vendedor Rafael: '))
Milena = float(input('Insira os valores de venda da vendedora Milena: '))

vendas = Emily + Larissa + Rafael + Milena
print('Faturamento total R$ = ', vendas)

#Salário fixo
salario_fixo_vendedor = 1000
salario_fixo_gerente = 2000


#Vendedora Emily:
if Emily < 5000:
    total_emily = Emily * 0.01 + salario_fixo_vendedor
    print('Salário da Emily (Vendedora) = R$', total_emily)
elif Emily >= 5000 and Emily < 10000:
    total_emily = Emily * 0.015 + salario_fixo_vendedor
    print('Salário da Emily (Vendedora) = R$', total_emily)
else:
    total_emily = Emily * 0.02 + salario_fixo_vendedor
    print('Salário da Emily (Vendedora) = R$', total_emily)

#Vendedora Larissa:
if Larissa < 5000:
    total_larissa = Larissa * 0.01 + salario_fixo_vendedor
    print('Salário da Larissa (Vendedora) = R$', total_larissa)
elif Larissa >= 5000 and Larissa < 10000:
    total_larissa = Larissa * 0.015 + salario_fixo_vendedor
    print('Salário da Larissa (Vendedora) = R$', total_larissa)
else:
    total_larissa = Larissa * 0.02 + salario_fixo_vendedor
    print('Salário da Larissa (Vendedora) = R$', total_larissa)

#Vendedor Rafael:
if Rafael < 5000:
    total_rafael = Rafael * 0.01 + salario_fixo_vendedor
    print('Salário da Rafael (Vendedor) = R$', total_rafael)
elif Rafael >= 5000 and Rafael < 10000:
    total_rafael = Rafael * 0.015 + salario_fixo_vendedor
    print('Salário da Rafael (Vendedor) = R$', total_rafael)
else:
    total_rafael = Rafael * 0.02 + salario_fixo_vendedor
    print('Salário do Rafael (Vendedor) = R$', total_rafael)


#Vendedora Milena:
if Milena < 5000:
    total_milena = Milena * 0.01 + salario_fixo_vendedor
    print('Salário da Milena (Vendedora) = R$', total_milena)
elif Milena >= 5000 and Milena < 10000:
    total_milena = Milena * 0.015 + salario_fixo_vendedor
    print('Salário da Milena (Vendedora) = R$', total_milena)
else:
    total_milena = Milena * 0.02 + salario_fixo_vendedor
    print('Salário do Milena (Vendedor) = R$', total_milena)



comissao_gerente = (vendas * 0.05) + salario_fixo_gerente
total_salarios = float(total_emily + total_larissa + total_milena + total_rafael + comissao_gerente)


print('Salário da Jéssica (gerente) = R$', comissao_gerente)
print('Total dos salários = ', total_salarios)
