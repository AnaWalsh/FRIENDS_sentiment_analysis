-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema project_friends
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema project_friends
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `project_friends` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema project_api
-- -----------------------------------------------------
USE `project_friends` ;

-- -----------------------------------------------------
-- Table `project_friends`.`Season`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_friends`.`Season` (
  `idSeason` INT NOT NULL AUTO_INCREMENT,
  `SeasonNumber` INT NOT NULL,
  PRIMARY KEY (`idSeason`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project_friends`.`Author`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_friends`.`Author` (
  `idAuthor` INT NOT NULL AUTO_INCREMENT,
  `AuthorName` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idAuthor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project_friends`.`Episodes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_friends`.`Episodes` (
  `idEpisodes` INT NOT NULL AUTO_INCREMENT,
  `EpTitle` VARCHAR(145) NOT NULL,
  `Season_idSeason` INT NOT NULL,
  PRIMARY KEY (`idEpisodes`),
  INDEX `fk_Episodes_Season_idx` (`Season_idSeason` ASC) VISIBLE,
  CONSTRAINT `fk_Episodes_Season`
    FOREIGN KEY (`Season_idSeason`)
    REFERENCES `project_friends`.`Season` (`idSeason`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project_friends`.`Quote`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_friends`.`Quote` (
  `idQuote` INT NOT NULL AUTO_INCREMENT,
  `quote_` VARCHAR(70) NOT NULL,
  `Author_idAuthor` INT NOT NULL,
  `Episodes_idEpisodes` INT NOT NULL,
  PRIMARY KEY (`idQuote`),
  INDEX `fk_Quote_Author1_idx` (`Author_idAuthor` ASC) VISIBLE,
  INDEX `fk_Quote_Episodes1_idx` (`Episodes_idEpisodes` ASC) VISIBLE,
  CONSTRAINT `fk_Quote_Author1`
    FOREIGN KEY (`Author_idAuthor`)
    REFERENCES `project_friends`.`Author` (`idAuthor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Quote_Episodes1`
    FOREIGN KEY (`Episodes_idEpisodes`)
    REFERENCES `project_friends`.`Episodes` (`idEpisodes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
