for i in `seq 1 12`; do
    awk -v var=$i '{if($1 == var || $1 ~/^ *#/) print $0}' NB_final_snp.vcf
done > NB_final_snp_chr$i.vcf
