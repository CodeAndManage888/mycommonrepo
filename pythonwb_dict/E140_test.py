      #!/bin/bash
      #**************************************************************
      # Date: 032724 (Expected Solution with 88 Lines of Code)      *
      # Title: Play Bingo                                           *
      # Status: Testing (In Progress / Testing / Working)           *
      # In this exercise you will write a program that simulates a  *
      # game of Bingo for a single card. Begin by generating a list *
      # of all of the valid Bingo calls (B1 through O75). Once the  *
      # list has been created you can randomize the order of its    *
      # elements by calling the shuffle function in the random      *
      # module. Then your program should consume calls out of the   *
      # list, crossing out numbers on the card, until the card      *
      # contains a crossed out line (horizontal, vertical or        *
      # diagonal). Simulate 1,000 games and report the minimum,     *
      # maximum and average number of calls that must be made       *
      # before the card wins. Import your solutions to Exercises    *
      # 138 and 139 when completing this exercise allow us to work  *
      # with data, without needing to enter it each time our program*
      # runs.                                                       *
      #                                                             *
      # Computed Result Validated:                                  *
      #**************************************************************
      import random
      #--------------------------------------------------------------
      def bingo_card_gen():
        import random
        bingo_card = {}
        bingo_card["B"] = random.sample(range(1,16),5)
        bingo_card["I"] = random.sample(range(16,31),5)
        bingo_card["N"] = random.sample(range(31,46),5)
        bingo_card["G"] = random.sample(range(46,61),5)
        bingo_card["O"] = random.sample(range(61,76),5)
        return bingo_card

      def bingo_card_check(bingo_card):
        if bingo_card["B"][0] + bingo_card["I"][1] + bingo_card["N"][2] + bingo_card["G"][3] + bingo_card["O"][4] == 0:
          return True
        elif bingo_card["B"][4] + bingo_card["I"][3] + bingo_card["N"][2] + bingo_card["G"][1] + bingo_card["O"][0] == 0:
          return True
        elif bingo_card["B"][0] + bingo_card["B"][1] + bingo_card[ "B"][2] + bingo_card["B"][3] + bingo_card["B"][4] == 0:
          return True
        elif bingo_card["I"][0] + bingo_card["I"][1] + bingo_card["I"][2] + bingo_card["I"][3] + bingo_card["I"][4] == 0:
          return True
        elif bingo_card["N"][0] + bingo_card["N"][1] + bingo_card["N"][2] + bingo_card["N"][3] + bingo_card["N"][4] == 0:
          return True
        elif bingo_card["G"][0] + bingo_card["G"][1] + bingo_card["G"][2] + bingo_card["G"][3] + bingo_card["G"][4] == 0:
          return True
        elif bingo_card["O"][0] + bingo_card["O"][1] + bingo_card[ "O"][2] + bingo_card["O"][3] + bingo_card["O"][4] == 0:
          return True
        elif bingo_card["B"][0] + bingo_card["I"][0] + bingo_card["N"][0] + bingo_card["G"][0] + bingo_card["O"][0] == 0:
          return True
        elif bingo_card["B"][1] + bingo_card["I"][1] + bingo_card["N"][1] + bingo_card["G"][1] + bingo_card["O"][1] == 0:
         return True
        elif bingo_card["B"][2] + bingo_card["I"][2] + bingo_card["N"][2] + bingo_card["G"][2] + bingo_card["O"][2] == 0:
         return True
        elif bingo_card["B"][3] + bingo_card["I"][3] + bingo_card["N"][3] + bingo_card["G"][3] + bingo_card["O"][3] == 0:
         return True
        elif bingo_card["B"][4] + bingo_card["I"][4] + bingo_card["N"][4] + bingo_card["G"][4] + bingo_card["O"][4] == 0:
         return True
        else:
         return False
      #--------------------------------------------------------------
      if __name__ == "__main__":
        #------------------------------------------------------------
        # Generate Random Number Bingo Call into a List:
        #------------------------------------------------------------
        x, ctr, ovr_ctr = 0, 0, 0
        bingo_draw = []
        data_list = []
        while x <= 75:
          x += 1
          if x < 16:
            bingo_draw.append("B" + str(x))
          elif x < 31:
            bingo_draw.append("I" + str(x))
          elif x < 46:
            bingo_draw.append("N" + str(x))
          elif x < 61:
            bingo_draw.append("G" + str(x))
          else:
            bingo_draw.append("O" + str(x))
        #print(bingo_draw)
        #------------------------------------------------------------
        # Generate a Bingo Card:
        #------------------------------------------------------------
        while ovr_ctr <= 1000:
          ovr_ctr += 1
          bingo_card = bingo_card_gen()
        #  print(bingo_card)
        #  print("B\tI\tN\tG\tO")
        #  for i in range(5):
        #    print(bingo_card["B"][i],"\t",bingo_card["I"][i],"\t",bingo_card["N"][i],"\t",bingo_card["G"][i],"\t",bingo_card["O"][i])
        #------------------------------------------------------------
        # Shuffle Bingo Numbers:
        #------------------------------------------------------------
          random.shuffle(bingo_draw)
        #  print(bingo_draw)
        #------------------------------------------------------------
        # Number Update:
        #------------------------------------------------------------
          for item in bingo_draw:
            ctr += 1
        #    print(item)
            if item[0] == "B" and int(item[1:]) in bingo_card["B"]:
              bingo_card["B"][bingo_card["B"].index(int(item[1:]))] = 0
            elif item[0] == "I" and int(item[1:]) in bingo_card["I"]:
              bingo_card["I"][bingo_card["I"].index(int(item[1:]))] = 0
            elif item[0] == "N" and int(item[1:]) in bingo_card["N"]:
              bingo_card["N"][bingo_card["N"].index(int(item[1:]))] = 0
            elif item[0] == "G" and int(item[1:]) in bingo_card["G"]:
              bingo_card["G"][bingo_card["G"].index(int(item[1:]))] = 0
            elif item[0] == "O" and int(item[1:]) in bingo_card["O"]:
              bingo_card["O"][bingo_card["O"].index(int(item[1:]))] = 0
            else:
              continue
          #------------------------------------------------------------
            if bingo_card_check(bingo_card) is False:
          #    print("No winning line.")a
              continue
            else:
          #    print("Winning line!")
              data_list.append(ctr)
              ctr = 0
              break
        #------------------------------------------------------------
        # Print the updated Bingo card:
        #------------------------------------------------------------
        #  print("B\tI\tN\tG\tO")
        #  for i in range(5):
        #    print(bingo_card["B"][i],"\t",bingo_card["I"][i],"\t",bingo_card["N"][i],"\t",bingo_card["G"][i],"\t",bingo_card["O"][i])
        #------------------------------------------------------------
        # Report Data:
        #------------------------------------------------------------
        print("=========================================================")
        print("Minimum number of calls:",min(data_list))
        print("Maximum number of calls:",max(data_list))
        print("Average number of calls:",sum(data_list)/len(data_list))
        print("=========================================================")
        print("Thank you for using this app.")