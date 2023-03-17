
from openai.OpenAiClient import OpenAiClient

def main():
    oc = OpenAiClient()
    oc.set_temperature(0.2)
    print(oc.temperature)

if __name__ == '__main__':
    main()
