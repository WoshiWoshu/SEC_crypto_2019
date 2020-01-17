##
## EPITECH PROJECT, 2019
## Makefile
## File description:
## Makefile
##

CHALLENGES	=	./chall01/challenge01 \
				./chall02/challenge02 \
				./chall03/challenge03 \
				./chall04/challenge04 \
				./chall05/challenge05 \
				./chall06/challenge06 \
				./chall07/challenge07 \
				./chall08/challenge08 \
				./chall09/challenge09 \
				./chall10/challenge10 \
				./chall11/challenge11 \
				./chall12/challenge12 \
				./chall13/challenge13 \
				./chall14/challenge14 \

COPY	=	$(shell cp -rf $(CHALLENGES) ./)

RIGHT	=	$(shell chmod +x $(CHALLENGES))

all	:	$(COPY) $(RIGHT)

clean	:
	rm -f *challenge* *.pyc *.pyo *~

fclean	:	clean

re	:	fclean
		$(COPY) $(RIGHT)

.PHONY	:	all clean fclean re
