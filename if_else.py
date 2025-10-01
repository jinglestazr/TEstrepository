while True:

    bill_amt=int(input('Enter The Bill Amount: '))


    if bill_amt>=50:
        print('Yes your able to get 10% discount, have a nice day')
        discount=bill_amt*0.1
        final_amt=bill_amt-discount
        print('Your discounted amt is: ', final_amt)
        print('Thanks for comign, please visit again')
    else:
        print('Sry your not eligiblee for the discount')
        print('Your bill is: ', bill_amt) 
        print('Thanks for comign, please visit again')
