outputfile='block_head.json'
echo '[' >${outputfile}
i_begin='300000'
i_end='501903'
for ((i=${i_begin}; i<= ${i_end}; i++ ))
do
hash=`./bitcoin-cli getblockhash ${i}`
#echo ${hasha}
if [ ${i} -lt 501903 ]; then
./bitcoin-cli getblockheader ${hash} | sed 's/}/},/' >>${outputfile}
else 
./bitcoin-cli getblockheader ${hash}  >>${outputfile}
fi
done
#sed -i 's/}/},/' ${outputfile}  
echo ']' >>${outputfile}
