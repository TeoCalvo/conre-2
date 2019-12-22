SELECT T1.numero_sequencial AS id_candidato,
        SUM( T1.valor ) AS patrimonio_candidato

FROM bens_candidatos AS T1

WHERE T1.ano_eleicao = {ano}

GROUP BY T1.numero_sequencial