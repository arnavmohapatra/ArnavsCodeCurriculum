import gpt_2_simple as gpt2

def gpt_output():
    session = gpt2.start_tf_sess()
    gpt2.load_gpt2(session)
    return gpt2.generate(session, length=100, temperature=0.7, prefix="Hello World,", nsamples=1 ,return_as_list=True)[0]

if __name__ == "__main__":
    print(gpt_output())